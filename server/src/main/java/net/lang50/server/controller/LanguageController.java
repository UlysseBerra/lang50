package net.lang50.server.controller;

import net.lang50.server.model.Language;
import net.lang50.server.repository.LanguageRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

@RestController
@CrossOrigin("*")
@RequestMapping("/")
public class LanguageController {
    @Autowired
    LanguageRepository languageRepository;

    @GetMapping("/languages")
    public ResponseEntity<List<Language>> getAllLanguages(@RequestParam(required = false) String name) {
        try {
            List<Language> languages = new ArrayList<Language>();

            if (name == null) {
                languageRepository.findAll().forEach(languages::add);
            } else {
                languageRepository.findByNameContaining(name).forEach(languages::add);
            }

            if (languages.isEmpty()) {
                return new ResponseEntity<>(HttpStatus.NO_CONTENT);
            }

            return new ResponseEntity<>(languages, HttpStatus.OK);
        } catch (Exception e) {
            return new ResponseEntity<>(null, HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }

    @PostMapping("/languages")
    public ResponseEntity<Language> createLanguage(@RequestBody Language language) {
        try {
            Language _language = languageRepository
                    .save(new Language(language.getName(), language.getAudio(), language.getScript()));
            return new ResponseEntity<>(_language, HttpStatus.CREATED);
        } catch (Exception e) {
            return new ResponseEntity<>(null, HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }

    @GetMapping("/languages/{id}")
    public ResponseEntity<Language> getLanguageById(@PathVariable("id") long id) {
        Optional<Language> languageData = languageRepository.findById(id);

        if (languageData.isPresent()) {
            return new ResponseEntity<>(languageData.get(), HttpStatus.OK);
        } else {
            return new ResponseEntity<>(HttpStatus.NOT_FOUND);
        }
    }
}
