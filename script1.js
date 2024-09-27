// cursor settings

var main = document.querySelector("#main");
var cursor = document.querySelector("#cursor");
var nav = document.querySelector(".nav");
var page = document.querySelector("#page2");

main.addEventListener("mousemove",function(dets){
    gsap.to(cursor,{
        x:dets.x,
        y:dets.y,
        duration:0.5,
    })
})

nav.addEventListener("mouseenter",function(){
    gsap.to(cursor,{
        scale:2,
        backgroundColor:"red"
    })
})

nav.addEventListener("mouseleave",function(){
    gsap.to(cursor,{
        scale:1,
        backgroundColor:"white"
    })
})


// norkmalj aihfsafasj

var tl = gsap.timeline()

tl.from(".nav h2",{
    y:-20,
    opacity:0,
    duration:0.8,
    delay:0.5,
})

tl.from(".nav h4",{
    y:-20,
    opacity:0,
    duration:0.5,
    stagger:0.2,
})

tl.from("#main h1",{
    y:20,
    duration:0.5,
    opacity:0,
    scale:0.2
})
tl.from("#main h3",{
    y:20,
    duration:0.5,
    opacity:0,
    scale:0.2
})
tl.from("#main span",{
    y:20,
    duration:0.5,
    opacity:0,
    scale:0.2
})


tl.to("#page3 h4",{
    transform:"translateX(-370%)",
    scrollTrigger:{
        trigger:"#page3",
        scroller:"body",
        markers:true,
        start:"top 0%",
        duration:0.4,
        end:"top -200%",
        scrub:2,
        pin:true

    }

})