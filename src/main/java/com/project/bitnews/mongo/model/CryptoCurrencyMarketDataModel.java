package com.project.bitnews.mongo.model;

import lombok.*;
import org.springframework.data.mongodb.core.mapping.Document;

@Getter
@Setter
@ToString
@AllArgsConstructor
@NoArgsConstructor
@Document(collection = "CryptoMarketData")
public class CryptoCurrencyMarketDataModel {
    String id;
    String symbol;
    String name;
    double price;
    long market_cap;
    long total_volume;
    int rank;
    String image;
    double high24h;
    double low24h;
    double priceChange24h;
    double priceChangePercentage24h;
    double marketCapChange24h;
    double marketCapChangePercentage24h;
    double circulatingSupply;
    double totalSupply;
    double maxSupply;
    double atl;
    double atlChangePercentage;
    String atlDate;
    String lastUpdated;

}
