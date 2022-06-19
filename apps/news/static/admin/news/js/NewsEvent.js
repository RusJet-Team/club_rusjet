jQuery(document).ready(function ($) {
    let idEventBool = $("#id_event_bool");
    let divHideEventDate = $(".form-row .field-event_date")
    let divHideGeoLocation = $(".form-row .field-geolocation_url")

    // exit from function if there isn't selector
    if (!idEventBool.length) {
        return false
    }
    // hide the field `pr_director_name`.
    divHideEventDate.hide();
    divHideGeoLocation.hide();

    function toggleDivDependedOnIsPrDirector(inputType) {
        if (inputType) {
            divHideEventDate.slideDown();
            divHideGeoLocation.slideDown();
        } else {
            divHideEventDate.slideUp();
            divHideGeoLocation.slideUp();
        }
    }

    // show/hide on load based on existing value of idIsPrDirector
    toggleDivDependedOnIsPrDirector(idEventBool.is(":checked"));

    // show/hide on change
    idEventBool.change(function () {
        toggleDivDependedOnIsPrDirector(idEventBool.is(":checked"));
    });
});
