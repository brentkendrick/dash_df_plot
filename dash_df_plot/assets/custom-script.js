// alert('If you see this alert, then your custom JavaScript script has run!')

// function toggle(id) {
//   var state = document.getElementById(id).style.fontSize
//   if (state == '20px') {
//     document.getElementById(id).style.fontSize = '10px'
//   } else {
//     document.getElementById(id).style.fontSize = '20px'
//   }
// }

// window.addEventListener('click', () => {
//   let thedesctitle = document.getElementById('page_title')
//   thedesctitle.setAttribute('onclick', "toggle('trace-html-download');")
// })

// function toggle2(id, classnm) {
//   document.getElementById(id).getElementsByClassName(classnm).style.background = 'rgb(51,255,0)'
// }

// window.addEventListener('click', () => {
//   let thedesctitle2 = document.getElementById('page_title')
//   thedesctitle2.setAttribute('onclick', "toggle2('Mygraph', '.js-plotly-plot > .plot-container.plotly > .user-select-none.svg-container > .main-svg');")
// })

// function download(filename, text) {
//   var element = document.createElement('a')
//   element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text))
//   element.setAttribute('download', filename)

//   element.style.display = 'none'
//   document.body.appendChild(element)

//   element.click()

//   document.body.removeChild(element)
// }

// jQuery.fn.outerHTML = function () {
//   return jQuery('<div />').append(this.eq(0).clone()).html()
// }

// var html = $('#div1').outerHTML()

// $('#divs').get(0).outerHTML

// function toggle3() {
//   let graphid = document.getElementById('Mygraph').children
//   download('js_params.html', $graphid.get(0).outerHTML)
// }

// function toggle3() {
//   let graphid = document.getElementById('Mygraph').children
//   console.log(graphid)
// }

// window.addEventListener('click', () => {
//   let pagetitle = document.getElementById('graphing-params-download')
//   pagetitle.setAttribute('onclick', 'toggle3();')
// })

// Not working below
// let label_text = document.getElementsByClassName('annotation-text'),
//   options = {
//     style: 'font-size: 20px',
//   },
//   observer = new MutationObserver(mCallback)

// function mCallback(mutations) {
//   for (let mutation of mutations) {
//     if (mutation.type === 'data-unformatted') {
//       console.log('Mutation Detected: A child node has been added or removed.')
//     }
//   }
// }

// observer.observe(label_text, options)
