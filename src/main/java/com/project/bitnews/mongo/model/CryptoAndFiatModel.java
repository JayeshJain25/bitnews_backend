package com.project.bitnews.mongo.model;

import lombok.*;
import org.springframework.data.mongodb.core.mapping.Document;

@Getter
@Setter
@ToString
@AllArgsConstructor
@NoArgsConstructor
@Document(collection = "CryptoFiatList")
public class CryptoAndFiatModel {
    String id;
    String symbol;
    String name;
    String price;
    String market_cap;
    String total_volume;
    String rank;
    String image;

}
