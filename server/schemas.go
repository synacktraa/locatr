package main

type llmSettings struct {
	LlmProvider    string `json:"llm_provider"`
	LlmApiKey      string `json:"llm_api_key"`
	ModelName      string `json:"model_name"`
	ReRankerApiKey string `json:"reranker_api_key"`
}

type locatrSettings struct {
	PluginType        string      `json:"plugin_type" binding:"required,oneof=selenium cdp"`
	CdpURl            string      `json:"cdp_url"`
	SeleniumUrl       string      `json:"selenium_url"`
	SeleniumSessionId string      `json:"selenium_session_id"`
	TabNo             int         `json:"tab_no"`
	CachePath         string      `json:"cache_path"`
	UseCache          bool        `json:"use_cache"`
	LlmSettings       llmSettings `json:"llm_settings"`
	ResultsFilePath   string      `json:"results_file_path"`
}

type incomingMessage struct {
	Type        string         `json:"type" binding:"required,oneof=initial_handshake locatr_request change_tab"`
	UserRequest string         `json:"user_request"`
	ClientId    string         `json:"id" binding:"required"`
	TabNo       string         `json:"tab_no"`
	Settings    locatrSettings `json:"locatr_settings"`
}

type outgoingMessage struct {
	Type     string `json:"type"`
	Status   string `json:"status"`
	ClientId string `json:"id"`
	Output   string `json:"output"`
	Error    string `json:"error"`
}
