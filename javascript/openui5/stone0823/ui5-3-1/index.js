sap.ui.define([
    "sap/m/Button"
], function (Button) {
    "use strict";

    var onButtonPressed = function (oEvent) {
        var oText = oEvent.getSource().getText()
        alert(oText)
    }
    new Button({
        text : "click me!",
        press : onButtonPressed
    }).placeAt("content")
})