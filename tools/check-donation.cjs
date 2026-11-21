const fs=require('node:fs');
const vm=require('node:vm');
const assert=require('node:assert/strict');
const source=fs.readFileSync(require('node:path').join(__dirname,'../assets/site.js'),'utf8');
for(const [url,active] of [[null,false],['',false],['not a url',false],['http://payment.example',false],['javascript:alert(1)',false],['https://payment.example/donate',true]]){
 const elements={
  '#donation-payment':{hidden:true},'#donation-pending':{hidden:false},
  '#donation-state':{},'#donation-explanation':{},'#donation-note':{}
 };
 vm.runInNewContext(source,{URL,window:{CAMPAIGN:{donationUrl:url}},document:{querySelector:selector=>elements[selector]||null}});
 assert.equal(elements['#donation-payment'].hidden,!active);
 assert.equal(elements['#donation-pending'].hidden,active);
 if(active)assert.equal(elements['#donation-payment'].href,url);
}
console.log('Donation gate: 6 configuration cases passed. No network requests or payments performed.');
