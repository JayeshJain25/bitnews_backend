package com.project.bitnews.controller;


import com.project.bitnews.mongo.model.CryptoAndFiatModel;
import com.project.bitnews.mongo.model.CryptoCurrencyMarketDataModel;
import com.project.bitnews.service.CryptoCurrencyService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
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
    public ResponseEntity<?> getAllCryptoAndFiatList(@RequestParam(defaultValue = "0") int page, @RequestParam(defaultValue = "10") int size) {

        List<CryptoAndFiatModel> allCryptoAndFiatList = cryptoCurrencyService.getAllCryptoAndFiatList(page,size);
        if (allCryptoAndFiatList != null)
            return ResponseEntity.status(HttpStatus.OK).body(allCryptoAndFiatList);
        else
            return ResponseEntity.status(HttpStatus.UNAUTHORIZED).body(null);

    }

    @GetMapping("/get-crypto-market-data-list")
    public ResponseEntity<?> getAllCryptoMarketDataList(@RequestParam(defaultValue = "0") int page, @RequestParam(defaultValue = "10") int size) {

        List<CryptoCurrencyMarketDataModel> cryptoCurrencyMarketData = cryptoCurrencyService.getCryptoCurrencyMarketData(page,size);
        if (cryptoCurrencyMarketData != null)
            return ResponseEntity.status(HttpStatus.OK).body(cryptoCurrencyMarketData);
        else
            return ResponseEntity.status(HttpStatus.UNAUTHORIZED).body(null);

    }

}
