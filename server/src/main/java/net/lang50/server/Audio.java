package net.lang50.server;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;

public class Audio {
    private final String name;

    private final byte[] audio;

    public Audio(String name, String audioPath) throws IOException {
        this.name = name;

        File f = new File(audioPath);
        this.audio = Files.readAllBytes(f.toPath());
    }

    public String getName() {
        return name;
    }

    public byte[] getAudio() {
        return audio;
    }
}
