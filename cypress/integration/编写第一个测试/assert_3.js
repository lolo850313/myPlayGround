/// <reference types="cypress" />

describe('my 1st test', function name() {
    it('find "type" ', function () {
        cy.visit('D:\\工作文档\\pdf结构化\\test.html')
        cy.contains('type').click()

        cy.url().should("include", "/commands/actions")
    })
})