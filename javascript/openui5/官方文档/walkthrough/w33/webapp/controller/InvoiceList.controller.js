sap.ui.define([
	"sap/ui/core/mvc/Controller",
	"sap/ui/model/json/JSONModel",
	"../model/formatter",
	"sap/ui/model/Filter",
	"sap/ui/model/FilterOperator"
], function (Controller, JSONModel, formatter, Filter, FilterOperator) {
	"use strict";

	return Controller.extend("sap.ui.demo.walkthrough.controller.InvoiceList", {
		formatter : formatter,
		onInit : function () {
			var oViewModel = new JSONModel({
				currency : "EUR"
			})

			this.getView().setModel(oViewModel, "view")
		},
		onFilterInvoices : function (oEvent) {
			var aFilter = []
			var sQuery = oEvent.getParameter("query")
			if (sQuery) {
				aFilter.push(new Filter("ProductName", FilterOperator.Contains, sQuery))
			}

			var oList = this.byId("invoiceList")
			var oBinding = oList.getBinding("items")
			oBinding.filter(aFilter)
		},
		onPress : function (oEvent) {
			var oRouter = this.getOwnerComponent().getRouter()
			// encodeURIComponent() 函数可把字符串作为 URI 组件进行编码。
			var oItem = oEvent.getSource()
			console.log(window.encodeURIComponent(oItem.getBindingContext("invoice").getPath().substr(1)))
			
			console.log(oItem.getBindingContext("invoice").getPath())

			console.log(oItem.getBindingContext("invoice") )

			oRouter.navTo("detail", {
				invoicePath : window.encodeURIComponent(oItem.getBindingContext("invoice").getPath().substr(1))
			})
		}
	});
});