/// <reference types="cypress" />

describe('my 1st test', function name() {
    it('find "type" ', function () {
        cy.visit('https://example.cypress.io')
        cy.contains('type').click()

        cy.url().should("include", "/commands/actions")
        cy.pause()
        cy.get('.action-email')
            // .type('fake@email.com')
            .should("have.value", 'fake@email.com')
    })
})