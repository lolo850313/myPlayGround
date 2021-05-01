sap.ui.require([
    "sap/ui/model/json/JSONModel",
    "sap/ui/core/mvc/XMLView",
    "sap/ui/model/BindingMode"
], function (JSONModel, XMLView, BindingMode) {
    "use strict";

    sap.ui.getCore().attachInit(function () {
        var oModel = new JSONModel({
            firstName : "Harry",
            lastName : "Hawk",
            enabled: true,
            panelHeaderText : "Data Binding Basics"
        })

        oModel.setDefaultBindingMode(BindingMode.OneWay)

        sap.ui.getCore().setModel(oModel)

        new XMLView({
            viewName : "sap.ui.demo.db.view.App"
        }).placeAt("content")
    })
})