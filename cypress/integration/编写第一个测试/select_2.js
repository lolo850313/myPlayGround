/// <reference types="cypress" />

describe('my 1st test', function name() {
    it('find "type" ', function () {
        cy.visit('https://example.cypress.io')
        cy.contains('type').click()
    })
})