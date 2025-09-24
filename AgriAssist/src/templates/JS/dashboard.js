function settingShow(elem, targetId) {
    categoriesSideElems = document.querySelectorAll(".categories ul li");
    detailSection = document.getElementsByClassName("profile-details")[0];
    allDetails = detailSection.querySelectorAll(".detailSection");
    categoriesSideElems.forEach(element => {
        element.classList.remove("active");
    });
    allDetails.forEach(element => {
        element.style.visibility = 'hidden';
    });
    elem.classList.add("active");
    detailSection.querySelector('#'+targetId).style.visibility = 'visible';
}