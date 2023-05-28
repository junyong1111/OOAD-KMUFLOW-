package com.project.kmuflow.GPT;

import lombok.Data;

import java.util.List;

@Data
public class GPTResponse {
    private List<GPTChoice> choicesList;
}
