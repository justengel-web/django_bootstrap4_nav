function is_small(){
    // Return if the screen size is small
    var mq = window.matchMedia('(max-width: 1200px)');
    return !!mq.matches;
}

function turn_off_container(){
    $('.container').toggleClass('container had-container');
    $('.card.hoverable').toggleClass('hoverable had-hoverable');
}

function turn_on_container(){
    $('.had-container').toggleClass('container had-container');
    $('.card.hoverable').toggleClass('hoverable had-hoverable');
}

function sidenav_small(){
    $('.collapsed.collapse.show').toggleClass('show');
}
function sidenav_fixed_small(){
    $('.sidenav-fixed').toggleClass('sidenav-fixed sidenav-fixed-small');
}


function check_size_for_container(){
    if (is_small()){
        // Window is small
        turn_off_container();
        sidenav_fixed_small();
    } else {
        // Window is large
        turn_on_container();
    }
}
