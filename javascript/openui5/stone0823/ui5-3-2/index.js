sap.ui.define([
    "sap/m/Button"
], function (Button) {
    "use strict";

    var onButtonPressed = function (oEvent) {
        var sId = oEvent.getSource().getId()
        if (sId === "btn1") {
            alert("hello from btn1")
        } else {
            alert("hello from btn2")
        }
    }
    new Button({
        text : "btn 1",
        id : "btn1",
        press : onButtonPressed
    }).placeAt("content")

    new Button({
        text : "btn 2",
        id : "btn2",
        press : onButtonPressed
    }).placeAt("content")
})