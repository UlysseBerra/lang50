package net.lang50.server.model;

import jakarta.persistence.*;

@Entity
@Table(name = "languages")
public class Language {
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private long id;

    @Column(name = "name")
    private String name;

    @Column(name = "audio")
    @Lob
    private byte[] audio;

    @Column(name = "script")
    @Lob
    private byte[] script;

    public Language() {

    }

    public Language(String name, byte[] audio, byte[] script) {
        this.name = name;
        this.audio = audio;
        this.script = script;
    }

    public long getId() {
        return id;
    }

    public void setId(long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public byte[] getAudio() {
        return audio;
    }

    public void setAudio(byte[] audio) {
        this.audio = audio;
    }

    public byte[] getScript() {
        return script;
    }

    public void setScript(byte[] script) {
        this.script = script;
    }

    @Override
    public String toString() {
        return "Language [id=" + id + ", title=" + name + ", audio=" + audio + ", script=" + script + "]";
    }
}
