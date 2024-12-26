import uuid
from enum import Enum
from typing import Optional, Union

from pydantic import BaseModel, Field, HttpUrl


class MessageType(str, Enum):
    INITIAL_HANDSHAKE = "initial_handshake"
    LOCATR_REQUEST = "locatr_request"
    CHANGE_TAB = "change_tab"


class OutputStatus(str, Enum):
    OK = "ok"
    ERROR = "error"


class LlmProvider(str, Enum):
    OPENAI = "openai"
    ANTHROPIC = "anthropic"


class PluginType(str, Enum):
    SELENIUM = "selenium"
    CDP = "cdp"


class Message(BaseModel):
    id: uuid.UUID
    type: MessageType


class OutputMessage(Message):
    status: OutputStatus
    error: str
    output: str


class LlmSettings(BaseModel):
    llm_provider: Optional[LlmProvider] = Field(default=None)
    llm_api_key: Optional[str] = Field(default=None)
    model_name: Optional[str] = Field(default=None)
    reranker_api_key: Optional[str] = Field(default=None)


class LocatrSettings(BaseModel):
    cache_path: Optional[str] = Field(default=None)
    use_cache: bool = Field(default=True)
    llm_settings: LlmSettings
    results_file_path: Optional[str] = Field(default=None)


class LocatrSeleniumSettings(LocatrSettings):
    selenium_url: HttpUrl
    selenium_session_id: str
    plugin_type: PluginType = PluginType.SELENIUM


class LocatrCdpSettings(LocatrSettings):
    cdp_url: HttpUrl
    plugin_type: PluginType = Field(default=PluginType.CDP)


class InitialHandshakeMessage(Message):
    locatr_settings: Union[LocatrSeleniumSettings, LocatrCdpSettings]


class UserRequestMessage(Message):
    user_request: str
