package com.project.bitnews.mongo.model;

import lombok.*;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

@Getter
@Setter
@ToString
@AllArgsConstructor
@NoArgsConstructor
@Document(collection = "CryptoFiatList")
public class CryptoAndFiatModel {
    @Id
    String id;
    String symbol;
    String name;
    double price;
    double marketCap;
    double totalVolume;
    double rank;
    String image;
}
