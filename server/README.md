# `lang50` API & database

## How to use

-   Configuration to avoid errors (to be solved in next revision of the code)
    -   check Java version used locally
    -   use correct local paths in `import.sql` and `application.properties`
-   Testing
    -   while in `server` directory, run `./mvnw spring-boot:run`
    -   API can then be accessed at `http://localhost:8080/languages`
-   Full build
    -   while in `server` directory, run:
    -   `./mvnw clean install`
    -   `cd target`
    -   `java -jar lang50-api-1.0.jar`
