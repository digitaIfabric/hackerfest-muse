(
SynthDef('synth', {
	arg freq;
	var sound = SinOsc.ar(freq, mul:0.2);
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