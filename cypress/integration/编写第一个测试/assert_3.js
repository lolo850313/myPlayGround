/// <reference types="cypress" />

describe('my 1st test', function name() {
    it('find "type" ', function () {
        cy.visit('D:\\�����ĵ�\\pdf�ṹ��\\test.html')
        cy.contains('type').click()

        cy.url().should("include", "/commands/actions")
    })
})