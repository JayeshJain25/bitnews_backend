package com.project.bitnews.mongo.model;


import lombok.*;
import org.springframework.data.mongodb.core.mapping.Document;

@Getter
@Setter
@ToString
@AllArgsConstructor
@NoArgsConstructor
@Document(collection = "NewsList")
public class NewsModel {
    String title;
    String source;
    String description;
    String publishedDate;
    String url;
    String photoUrl;
    String summary;
    String readTime;
}
