package net.lang50.server;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.io.IOException;

@RestController
public class ScriptController {
    @GetMapping("/script")
    public Script script() throws IOException {
        return new Script("LanguageName", "/Users/ulysseberra/Documents/Code/lang50/server/src/main/resources/static/tmp.jpg");
    }
}
