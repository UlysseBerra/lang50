package net.lang50.server.repository;

import net.lang50.server.model.Language;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface LanguageRepository extends JpaRepository<Language, Long> {
    List<Language> findByNameContaining(String name);
}
