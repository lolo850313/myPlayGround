sap.ui.define([
	"sap/ui/core/mvc/Controller",
	"sap/m/MessageToast",
	"sap/m/MessageBox",
	"sap/ui/model/Sorter",
	"sap/ui/model/Filter",
	"sap/ui/model/FilterOperator",
	"sap/ui/model/FilterType",
	"sap/ui/model/json/JSONModel"
], function (Controller, MessageToast, MessageBox, Sorter, Filter, FilterOperator, FilterType, JSONModel) {
	"use strict";

	return Controller.extend("sap.ui.core.tutorial.odatav4.controller.App", {

		/**
		 *  Hook for initializing the controller
		 */
		onInit : function () {
			var oMessageManager = sap.ui.getCore().getMessageManager(),
				oMessageModel = oMessageManager.getMessageModel(),
				oMessageModelBinding = oMessageModel.bindList("/", undefined, [], new Filter("technical", FilterOperator.EQ, true))

			oViewModel = new JSONModel({
				busy : false,
				hasUIChanges : false,
				usernameEmpty : true,
				order : 0
			})
			

			this.getView().setModel(oViewModel, "appView");
			this.getView().setModel(oMessageModel, "message");
			oMessageModelBinding.attachChange(this.onMessageBindingChange, this)
			this._bTechnicalErrors = false
		},

		onCreate : function () {
			var oList = this.byId("peopleList"),
				oBinding = oList.getBinding("items"),
				oContext = oBinding.create({
					"UserName" : "",
					"FirstName" : "",
					"LastName":"",
					"Age": 18
				})

		},

		onRefresh : function () {
			var oBinding = this.byId("peopleList").getBinding("items")

			if (oBinding.hasPendingChanges()) {
				MessageBox.error(this._getText("refreshNotPossibleMessage"))
				return
			}
			oBinding.refresh()
			MessageToast.show(this._getText("refreshSuccessMessage"))
		},

		onSearch : function () {
			var oView = this.getView(),
				sValue = oView.byId("searchField").getValue(),
				oFilter = new Filter("LastName", FilterOperator.Contains, sValue)

			oView.byId("peopleList").getBinding("items").filter(oFilter, FilterType.Application)
		},

		onSort : function () {
			var oView = this.getView(),
				aStates = [undefined, "asc", "desc"],
				aStateTextIds = ["sortNone", "sortAscending", "sortDescending"],
				sMessage,
				iOrder = oView.getModel("appView").getProperty("/order")

			iOrder = (iOrder + 1) % aStates.length
			var sOrder = aStates[iOrder]

			oView.getModel("appView").setProperty("/order", iOrder)
			oView.byId("peopleList").getBinding("items").sort(sOrder && new Sorter("LastName", sOrder === "desc"))

			sMessage = this._getText("sortMessage", [this._getText(aStateTextIds[iOrder])])
			// console.log(oView);
			// console.log(sMessage);
			// console.log(iOrder);
			// console.log(sOrder);
			// console.log(sMessage);
			MessageToast.show(sMessage)
		},

		_getText : function (sTextId, aArgs) {
			// console.log(sTextId, aArgs)
			return this.getOwnerComponent().getModel("i18n").getResourceBundle().getText(sTextId, aArgs)
		},

		_setUIChanges: function (bHasChanges) {
			if (this._bTechnicalErrors) {
				bHasChanges = true
			} else if (bHasChanges === undefined){
				bHasChanges = this.getView().getModel().hasPendingChanges()
			}

			var oModel = this.getView().getModel("appView")
			oModel.setProperty("/hasUIChanges", bHasChanges)
		}
	});
});