package net.lang50.server;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;

public class Script {
    private final String name;

    private final byte[] image;

    public Script(String name, String imagePath) throws IOException {
        this.name = name;

        File f = new File(imagePath);
        this.image = Files.readAllBytes(f.toPath());
    }

    public String getName() {
        return name;
    }

    public byte[] getImage() {
        return image;
    }
}
