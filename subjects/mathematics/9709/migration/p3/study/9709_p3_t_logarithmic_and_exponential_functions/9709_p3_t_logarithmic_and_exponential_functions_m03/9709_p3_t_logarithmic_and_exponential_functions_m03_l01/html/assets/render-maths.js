document.addEventListener('DOMContentLoaded',()=>{
  document.querySelectorAll('.math[data-tex]').forEach(el=>{
    katex.render(el.dataset.tex,el,{displayMode:el.classList.contains('display-math'),throwOnError:false,output:'htmlAndMathml'});
  });
  const svg=document.querySelector('#root-plot');
  if(svg){
    const sx=x=>100+(x/4)*520;
    const sy=y=>360-((y+3)/5.5)*330;
    const makePath=(fn,start,end,steps)=>Array.from({length:steps+1},(_,i)=>{
      const x=start+(end-start)*i/steps;
      return `${i?'L':'M'}${sx(x).toFixed(1)},${sy(fn(x)).toFixed(1)}`;
    }).join(' ');
    svg.querySelector('#log-curve').setAttribute('d',makePath(Math.log,0.05,4,120));
    svg.querySelector('#parabola-curve').setAttribute('d',makePath(x=>3*x-x*x,0,4,120));
  }
});
