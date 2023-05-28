package com.project.kmuflow.GPT;

import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@Slf4j
@RequestMapping("/gpt")
@Controller
public class GPTController
{
    private GPTService gptService;

    public GPTController(GPTService gptService){
        this.gptService = gptService;
    }
    @PostMapping("/question")
    public String searchGPT(@RequestBody SearchRequest searchRequest){
        return gptService.processSearch(searchRequest.getQuery());
    }
}
