// Basic Synth Definition
(
SynthDef('synth', {
	arg freq;
	var sound = SinOsc.ar(freq, mul:0.2);
	var linen = Env.linen(0.01, 0, 1);
	var env = EnvGen.kr(linen, doneAction:2);
	Out.ar(0, sound * env);
}).add;
)

//SynthDef Plucking
/*(
SynthDef("plucking", {arg amp = 0.1, freq = 440, decay = 5, coef = 0.1;
var env, snd;
env = EnvGen.kr(Env.linen(0, decay, 0.5), doneAction: 2);
snd = Pluck.ar(
        in: Saw.ar(freq, 0.5*amp),
        trig: Impulse.kr(0),
        maxdelaytime: 0.1,
        delaytime: freq.reciprocal,
        decaytime: decay,
        coef: coef);
    Out.ar(0, [snd, snd]);
}).add;
)*/

(
OSCdef('alphabrain', {
	arg msg;
	Synth('synth', [freq:msg[1]]);
}, "/beep");
)

/*(
OSCdef('betabrain', {
	arg msg;
	Synth('plucking', [freq:msg[1]]);
}, "/bbeep");
)*/