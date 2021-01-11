var swiper = new Swiper(".swiper-container", {
        navigation: {
            nextEl: ".swiper-button-next",
            prevEl: ".swiper-button-prev"
        }
    }), latitude = document.getElementById("map").dataset.latitude,
    longitude = document.getElementById("map").dataset.longitude;

function init() {
    var e = new ymaps.Map("map", {center: [latitude, longitude], zoom: 10}, {searchControlProvider: "yandex#search"}),
        t = new ymaps.GeoObject({geometry: {type: "Point", coordinates: [latitude, longitude]}});
    e.geoObjects.add(t)
}

function validateEmail(e) {
    return /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(String(e).toLowerCase())
}

function blurEvent(e) {
    e.setAttribute("placeholder", ""), "" == e.value && e.classList.add("error")
}

function onChangeEvent(e) {
    "" == e.value ? e.classList.add("error") : e.classList.remove("error"), "email" == e.id && (validateEmail(e.value) ? e.classList.remove("error") : e.classList.add("error"))
}

function onSubmitEvent() {
    var e = document.getElementById("name"), t = document.getElementById("email");
    "" != e.value && validateEmail(t.value) ? document.getElementById("form").submit() : ("" == e.value ? e.classList.add("error") : e.classList.remove("error"), validateEmail(t.value) ? t.classList.remove("error") : t.classList.add("error"))
}

ymaps.ready(init);