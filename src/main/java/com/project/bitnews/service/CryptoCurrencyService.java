package com.project.bitnews.service;


import com.project.bitnews.mongo.model.CryptoAndFiatModel;
import com.project.bitnews.mongo.repository.CryptoAndFiatRepository;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.RequestParam;

import java.util.List;

@Slf4j
@Service
public class CryptoCurrencyService {

    public static final String DB_NAME_CRYPT_LIST = "CryptoFiatList";

    @Autowired
    MongoTemplate mongoTemplate;

    @Autowired
    CryptoAndFiatRepository cryptoAndFiatRepository;

    public List<CryptoAndFiatModel> getAllCryptoAndFiatList(int page, int size) {
        Page<CryptoAndFiatModel> cryptoAndFiatModelPage;
        Pageable paging = PageRequest.of(page, size);
        cryptoAndFiatModelPage = cryptoAndFiatRepository.findAll(paging);
        return cryptoAndFiatModelPage.getContent();
    }
}
