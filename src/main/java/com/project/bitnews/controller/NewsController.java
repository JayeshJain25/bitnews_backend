package com.project.bitnews.controller;

import com.project.bitnews.mongo.model.CryptoAndFiatModel;
import com.project.bitnews.service.NewsService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("/news")
public class NewsController {

    private final NewsService newsService;

    @Autowired
    NewsController(NewsService newsService) {
        this.newsService = newsService;
    }

    @GetMapping("/get-list")
    public ResponseEntity<?> getAllCryptoAndFiatList() {

        List<CryptoAndFiatModel> getUserCreateCampaignDetails = newsService.getAllCryptoAndFiatList();
        if (getUserCreateCampaignDetails != null)
            return ResponseEntity.status(HttpStatus.OK).body(getUserCreateCampaignDetails);
        else
            return ResponseEntity.status(HttpStatus.UNAUTHORIZED).body(null);

    }

}