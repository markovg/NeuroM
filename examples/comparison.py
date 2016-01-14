# Copyright (c) 2015, Ecole Polytechnique Federale de Lausanne, Blue Brain Project
# All rights reserved.
#
# This file is part of NeuroM <https://github.com/BlueBrain/NeuroM>
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#     1. Redistributions of source code must retain the above copyright
#        notice, this list of conditions and the following disclaimer.
#     2. Redistributions in binary form must reproduce the above copyright
#        notice, this list of conditions and the following disclaimer in the
#        documentation and/or other materials provided with the distribution.
#     3. Neither the name of the copyright holder nor the names of
#        its contributors may be used to endorse or promote products
#        derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

def boxplots(object1, object2, feature_list, new_fig=True, subplot=False):
    '''Plots a list of boxplots for each feature in feature_list for object 1.
    Then presents the value of object 2 for each feature as an colored objected
    in the same boxplot.

    Parameters:
        object1: list\
            List of neurons, which can be reduced to one neuron.
        object2 : list\
            List of neurons, which can be reduced to one neuron.
        feature_list : list\
            List of strings, representing the features of interest.
        new_fig (Optional[bool]):\
            Default is False, which returns the default matplotlib axes 111\
            If a subplot needs to be specified, it should be provided in xxx format.
        subplot (Optional[bool]):\
            Default is False, which returns a matplotlib figure object. If True,\
            returns a matplotlib axis object, for use as a subplot.

    Returns:
        fig:\
            A figure which contains the list of boxplots.
    '''
    fig, ax = common.get_figure(new_fig=new_fig, subplot=subplot)

    # def funct(tr, feat='remote_bifurcation_angle'):
    #    return list(getattr(morphtree,'i_'+feat)(tr))

    # [funct(tr1, feat=f) for f in ['remote_bifurcation_angle', 'local_bifurcation_angle'] for tr1 in tr]

    # obj1_data = [getattr(object1, 'get_' + feature)() for neu in neurons]

    #    ax.boxplot(feature_values)

    #    x_labels = ['neuron_id' for _ in neurons]

    #    ax.set_xticklabels(x_labels)

    return fig, ax
