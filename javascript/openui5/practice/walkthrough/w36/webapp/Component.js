sap.ui.define([
	"sap/ui/core/UIComponent",
	"sap/ui/model/json/JSONModel",
	"./controller/HelloDialog",
	"sap/ui/Device"
], function (UIComponent, JSONModel, HelloDialog, Device) {
	"use strict";

	return UIComponent.extend("sap.ui.demo.walkthrough.Component", {

		metadata : {
			manifest: "json"
		},

		init : function () {
			// call the init function of the parent
			UIComponent.prototype.init.apply(this, arguments);

			// set data model
			var oData = {
				recipient : {
					name : "World @view component.js"
				}
			};
			var oModel = new JSONModel(oData);
			this.setModel(oModel);

			// this.getModel("invoice").setUseBatch(false)


			var oDeviceModel = new JSONModel(Device)
			oDeviceModel.setDefaultBindingMode("OneWay")
			this.setModel(oDeviceModel, "device")

			this._helloDialog = new HelloDialog(this.getRootControl())

			this.getRouter().initialize()
		},

		exit : function () {
			this._helloDialog.destroy()
			delete this._helloDialog
		},

		// openHelloDialog : function () {
		// 	this._helloDialog.open()	
		// }
	});
});