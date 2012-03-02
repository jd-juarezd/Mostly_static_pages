Feature: Rocking with lettuce and django

    Scenario: Prueba Home
        Given I access the url "/home/"
        Then I see the header "Pages#home"

 	Scenario: Prueba Contact
        Given I access the url "/contact/"
        Then I see the header "Pages#contact"
    
    Scenario: Prueba About
        Given I access the url "/about/"
        Then I see the header "Pages#about"

    
