package com.project.bitnews.controller;


import com.project.bitnews.mongo.model.CryptoAndFiatModel;
import com.project.bitnews.service.CryptoCurrencyService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("/cryptocurrency")
public class CryptoCurrencyController {

    private final CryptoCurrencyService cryptoCurrencyService;

    @Autowired
    CryptoCurrencyController(CryptoCurrencyService cryptoCurrencyService) {
        this.cryptoCurrencyService = cryptoCurrencyService;
    }

    @GetMapping("/get-crypto-fiat-list")
    public ResponseEntity<?> getAllCryptoAndFiatList() {

        List<CryptoAndFiatModel> allCryptoAndFiatList = cryptoCurrencyService.getAllCryptoAndFiatList();
        if (allCryptoAndFiatList != null)
            return ResponseEntity.status(HttpStatus.OK).body(allCryptoAndFiatList);
        else
            return ResponseEntity.status(HttpStatus.UNAUTHORIZED).body(null);

    }

}
