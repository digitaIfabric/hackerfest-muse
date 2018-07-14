(
SynthDef('synth', {
	arg freq;
	var sound = {SinOsc.ar(OnePole.ar(Mix(
LFSaw.ar([1,0.99],[0,0.6],2000,2000).trunc([400,600])*[1,-1]
),0.98)).dup*0.1};
	var linen = Env.linen(0.01, 0, 1);
	var env = EnvGen.kr(linen, doneAction:2);
	Out.ar(0, sound * env);
}).add;
)

(
OSCdef('brainpeep', {
	arg msg;
	Synth('synth', [freq:msg[1]]);
}, "/beep");
)