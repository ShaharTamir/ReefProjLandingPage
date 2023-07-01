

window.smoothScroll = function(target) {
    var scrollContainer = target;
    do { //find scroll container
        scrollContainer = scrollContainer.parentNode;
        if (!scrollContainer) return;
        scrollContainer.scrollTop += 1;
    } while (scrollContainer.scrollTop == 0);

    var targetY = 0;
    do { //find the top of target relatively to the container
        if (target == scrollContainer) break;
        targetY += target.offsetTop;
    } while (target = target.offsetParent);

    scroll = function(c, a, b, i) {
        i++; if (i > 30) return;
        c.scrollTop = a + (b - a) / 30 * i;
        setTimeout(function(){ scroll(c, a, b, i); }, 10);
    }
    // start scrolling
    scroll(scrollContainer, scrollContainer.scrollTop, targetY, 0);
}

function enable_send() {
    checkbox = document.getElementById("check");
    email = document.getElementById("user_email");
    user_name = document.getElementById("user_name");
    checkbox_bg = document.getElementById("checkbox-bg");
    button = document.getElementById("submit-button");

    if(checkbox.checked) {
        checkbox_bg.style.borderColor = "#FE9400";
        checkbox_bg.style.backgroundColor = "#FE9400";
    } else {
        button.style.borderColor = "transparent";
        button.style.background = "rgba(255, 255, 255, 0.15)";
        button.disabled = true;

        checkbox_bg.style.borderColor = "white";
        checkbox_bg.style.backgroundColor = "transparent";
    }

    if(checkbox.checked && email.value.length > 5 && user_name.value.length > 1) {
        button.style.borderColor = "#EFEFEF";
        button.style.background = "linear-gradient(to bottom right, transparent, #EFEFEF)";
        button.disabled = false;
    } else {
        button.style.borderColor = "transparent";
        button.style.background = "rgba(255, 255, 255, 0.15)";
        button.disabled = true;
    }
}
