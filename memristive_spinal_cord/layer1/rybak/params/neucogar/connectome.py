import neucogar.namespaces as NEST_NAMESPACE
from neucogar.SynapseModel import SynapseModel
from memristive_spinal_cord.layer1.rybak.neuron_group_names import Layer1NeuronGroupNames

stdp_glu = {'delay': 2.5,  # Synaptic delay
            'alpha': 1.0,  # Coeficient for inhibitory STDP time (alpha * lambda)
            'lambda': 0.0005,  # Time interval for STDP
            'Wmax': 300,  # Maximum possible weight
            'mu_minus': 0.005,  # STDP depression step
            'mu_plus': 0.005  # STDP potential step
            }
stdp_gaba = {'delay': 1.25,  # Synaptic delay
             'alpha': 1.0,  # Coeficient for inhibitory STDP time (alpha * lambda)
             'lambda': 0.0075,  # Time interval for STDP
             'Wmax': -300.0,  # Maximum possible weight
             'mu_minus': 0.005,  # STDP depression step
             'mu_plus': 0.005  # STDP potential step
             }

# synapses
Glutamatergic = SynapseModel(
    "Glutamatergic",
    nest_model=NEST_NAMESPACE.STDP_SYNAPSE,
    params=stdp_glu
)
GABAergic = SynapseModel(
    "GABAergic",
    nest_model=NEST_NAMESPACE.STDP_SYNAPSE,
    params=stdp_gaba
)

weight_Glu = 185
weight_GABA = -70


def connect(neuron_network):
    # source is FLEX_MOTOR
    neuron_network.connect(
        source=Layer1NeuronGroupNames.FLEX_MOTOR,
        target=Layer1NeuronGroupNames.FLEX_RENSHAW,
        synapse=Glutamatergic,
        weight=weight_Glu
    )
    # source is EXTENS_MOTOR
    neuron_network.connect(
        source=Layer1NeuronGroupNames.EXTENS_MOTOR,
        target=Layer1NeuronGroupNames.EXTENS_RENSHAW,
        synapse=Glutamatergic,
        weight=weight_Glu
    )

    # source is FLEX_RENSHAW
    neuron_network.connect(
        source=Layer1NeuronGroupNames.FLEX_RENSHAW,
        target=Layer1NeuronGroupNames.FLEX_MOTOR,
        synapse=GABAergic,
        weight=weight_GABA
    )
    neuron_network.connect(
        source=Layer1NeuronGroupNames.FLEX_RENSHAW,
        target=Layer1NeuronGroupNames.EXTENS_RENSHAW,
        synapse=GABAergic,
        weight=weight_GABA
    )
    neuron_network.connect(
        source=Layer1NeuronGroupNames.FLEX_RENSHAW,
        target=Layer1NeuronGroupNames.FLEX_INTER_1A,
        synapse=GABAergic,
        weight=weight_GABA
    )

    # source is EXTENS_RENSHAW
    neuron_network.connect(
        source=Layer1NeuronGroupNames.EXTENS_RENSHAW,
        target=Layer1NeuronGroupNames.EXTENS_MOTOR,
        synapse=GABAergic,
        weight=weight_GABA
    )
    neuron_network.connect(
        source=Layer1NeuronGroupNames.EXTENS_RENSHAW,
        target=Layer1NeuronGroupNames.FLEX_RENSHAW,
        synapse=GABAergic,
        weight=weight_GABA
    )
    neuron_network.connect(
        source=Layer1NeuronGroupNames.EXTENS_RENSHAW,
        target=Layer1NeuronGroupNames.EXTENS_INTER_1A,
        synapse=GABAergic,
        weight=weight_GABA
    )

    # source is FLEX_INTER_1A
    neuron_network.connect(
        source=Layer1NeuronGroupNames.FLEX_INTER_1A,
        target=Layer1NeuronGroupNames.EXTENS_MOTOR,
        synapse=GABAergic,
        weight=weight_GABA
    )
    neuron_network.connect(
        source=Layer1NeuronGroupNames.FLEX_INTER_1A,
        target=Layer1NeuronGroupNames.EXTENS_INTER_1A,
        synapse=GABAergic,
        weight=weight_GABA
    )

    # source is EXTENS_INTER_1A
    neuron_network.connect(
        source=Layer1NeuronGroupNames.EXTENS_INTER_1A,
        target=Layer1NeuronGroupNames.FLEX_MOTOR,
        synapse=GABAergic,
        weight=weight_GABA
    )
    neuron_network.connect(
        source=Layer1NeuronGroupNames.EXTENS_INTER_1A,
        target=Layer1NeuronGroupNames.FLEX_INTER_1A,
        synapse=GABAergic,
        weight=weight_GABA
    )

    # source is FLEX_INTER_1B
    neuron_network.connect(
        source=Layer1NeuronGroupNames.FLEX_INTER_1B,
        target=Layer1NeuronGroupNames.FLEX_MOTOR,
        synapse=GABAergic,
        weight=weight_GABA
    )
    neuron_network.connect(
        source=Layer1NeuronGroupNames.FLEX_INTER_1B,
        target=Layer1NeuronGroupNames.EXTENS_INTER_1B,
        synapse=GABAergic,
        weight=weight_GABA
    )

    # source is EXTENS_INTER_1B
    neuron_network.connect(
        source=Layer1NeuronGroupNames.EXTENS_INTER_1B,
        target=Layer1NeuronGroupNames.EXTENS_MOTOR,
        synapse=GABAergic,
        weight=weight_GABA
    )
    neuron_network.connect(
        source=Layer1NeuronGroupNames.EXTENS_INTER_1B,
        target=Layer1NeuronGroupNames.FLEX_INTER_1B,
        synapse=GABAergic,
        weight=weight_GABA
    )
