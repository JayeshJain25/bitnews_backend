package com.project.bitnews.utils.csv;

import com.project.bitnews.mongo.model.CryptoAndFiatModel;
import org.apache.commons.csv.CSVFormat;
import org.apache.commons.csv.CSVParser;
import org.apache.commons.csv.CSVRecord;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class CryptoCurrencyListCsv {

    public static List<CryptoAndFiatModel> parseCsvFile(InputStream is) {
        BufferedReader fileReader = null;
        CSVParser csvParser = null;

        List<CryptoAndFiatModel> cryptoAndFiatModelArrayList = new ArrayList<>();

        try {
            fileReader = new BufferedReader(new InputStreamReader(is, "UTF-8"));
            csvParser = new CSVParser(fileReader,
                    CSVFormat.DEFAULT.withFirstRecordAsHeader().withIgnoreHeaderCase().withTrim());

            Iterable<CSVRecord> csvRecords = csvParser.getRecords();

            for (CSVRecord csvRecord : csvRecords) {
                CryptoAndFiatModel customer = new CryptoAndFiatModel(
                        csvRecord.get("id"),
                        csvRecord.get("symbol"),
                        csvRecord.get("name"),
                        Double.parseDouble(csvRecord.get("price")),
                        Double.parseDouble(csvRecord.get("market_cap")),
                        Double.parseDouble(csvRecord.get("total_volume")),
                        Integer.parseInt(csvRecord.get("rank")),
                        csvRecord.get("image"));
                cryptoAndFiatModelArrayList.add(customer);
            }

        } catch (Exception e) {
            System.out.println("Reading CSV Error!");
            e.printStackTrace();
        } finally {
            try {
                assert fileReader != null;
                fileReader.close();
                assert csvParser != null;
                csvParser.close();
            } catch (IOException e) {
                System.out.println("Closing fileReader/csvParser Error!");
                e.printStackTrace();
            }
        }

        return cryptoAndFiatModelArrayList;
    }

}
