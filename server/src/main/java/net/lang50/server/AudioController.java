package net.lang50.server;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.io.IOException;

@RestController
public class AudioController {
    @GetMapping("/audio")
    public Audio audio() throws IOException {
        return new Audio("LanguageName", "/Users/ulysseberra/Documents/Code/lang50/server/src/main/resources/static/tmp.mp3");
    }
}