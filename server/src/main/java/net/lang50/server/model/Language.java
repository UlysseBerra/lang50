package net.lang50.server.model;

import jakarta.persistence.*;

import java.sql.Blob;

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
    private Blob audio;

    @Column(name = "script")
    private Blob script;

    public Language(String name, Blob audio, Blob script) {
        this.name = name;
        this.audio = audio;
        this.script = script;
    }

    public long getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Blob getAudio() {
        return audio;
    }

    public void setAudio(Blob audio) {
        this.audio = audio;
    }

    public Blob getScript() {
        return script;
    }

    public void setScript(Blob script) {
        this.script = script;
    }

    @Override
    public String toString() {
        return "Language [id=" + id + ", title=" + name + ", audio=" + audio + ", script=" + script + "]";
    }
}
