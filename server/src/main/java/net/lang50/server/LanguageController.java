package net.lang50.server;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.io.IOException;

@RestController
public class LanguageController {
    @GetMapping("/lang")
    public Language lang() throws IOException {
        return new Language("LanguageName", "/Users/ulysseberra/Documents/Code/lang50/server/src/main/resources/static/tmp.mp3", "/Users/ulysseberra/Documents/Code/lang50/server/src/main/resources/static/tmp.jpg");
    }
}