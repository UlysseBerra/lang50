package net.lang50.server;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;

public class Language {
    private final String name;
    private final byte[] audio;
    private final byte[] text;


    public Language(String name, String audioPath, String textPath) throws IOException {
        this.name = name;

        File fAudio = new File(audioPath);
        this.audio = Files.readAllBytes(fAudio.toPath());

        File fText = new File(textPath);
        this.text = Files.readAllBytes(fText.toPath());
    }

    public String getName() {
        return name;
    }

    public byte[] getAudio() {
        return audio;
    }

    public byte[] getText() {
        return text;
    }
}
