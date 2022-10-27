def filter(in_stream, out_stream_gum, out_stream_remaining, gum):
    'gum filter function, inputs (in_stream, gum stream, rest out)'
    # simple mass balance for gum
    gum_delta_filter = in_stream.mol_flow * in_stream.gum_frac
    gum_massflow = out_stream_gum.gum_molflow * gum.mr_kg

    # remaining stream
    new_molflow_filter = in_stream.mol_flow * (1 - in_stream.gum_frac)
    new_massflow_filter = in_stream.mass_flow - gum_massflow

    # update(new_massflow, new_molflow, co_delta, aco_delta, dco_delta, aa_delta, water_delta, gum_delta)
    out_stream_gum.update(new_massflow = gum_massflow, new_molflow = gum_delta_filter, gum_delta = gum_delta_filter)
    out_stream_remaining.update(new_massflow = new_massflow_filter, new_molflow = new_molflow_filter, gum_delta = (-1 * gum_delta_filter))
    return None


def column1(in_stream, out_stream_top, out_stream_bottom, aa, co, dco, aco, water):
    'args(instream, topstream, bottomstream, chemicals: aa, co, dco, aco, water'
    # separation 'efficiencies'
    water_delta_column1 = in_stream.water_molflow
    aa_delta_column1 = in_stream.aa_molflow
    co_delta_column1 = in_stream.co_molflow * 0.005 # <--- separation factors
    dco_delta_column1 = in_stream.dco_molflow * 0.95
    aco_delta_column1 = in_stream.aco_molflow * 0.002

    # top stream
    out_stream_top_molflow = water_delta_column1 + aa_delta_column1 + co_delta_column1 + dco_delta_column1 + aco_delta_column1
    out_stream_top_massflow = water_delta_column1*water.mr_kg + aa_delta_column1*aa.mr_kg + co_delta_column1*co.mr_kg + dco_delta_column1*dco.mr_kg + aco_delta_column1*aco.mr_kg
    out_stream_top.update(new_massflow = out_stream_top_massflow, new_molflow = out_stream_top_molflow, co_delta = co_delta_column1, aco_delta = aco_delta_column1, dco_delta = dco_delta_column1, aa_delta = aa_delta_column1, water_delta = water_delta_column1)

    #b ottom stream
    out_stream_bottom_massflow = in_stream.mass_flow - out_stream_top_massflow
    out_stream_bottom_molflow = in_stream.mol_flow - out_stream_top_molflow
    bottom_delta_co = in_stream.co_molflow * 0.995
    bottom_delta_dco = in_stream.dco_molflow * 0.05
    bottom_delta_aco = in_stream.aco_molflow * 0.998
    out_stream_bottom.update(new_massflow = out_stream_bottom_massflow, new_molflow = out_stream_bottom_molflow, co_delta = bottom_delta_co, dco_delta = bottom_delta_dco, aco_delta = bottom_delta_aco)
    return None


def column2(in_stream, out_stream_top, out_stream_bottom, aa, water):
    'args(instream, topstream, bottomstream, chemicals:aa, water'
    # separation top
    water_delta_column2 = in_stream.water_molflow
    aa_delta_column2 = in_stream.aa_molflow
    top_molflow = water_delta_column2 + aa_delta_column2
    top_massflow = water_delta_column2*water.mr_kg + aa_delta_column2*aa.mr_kg
    out_stream_top.update(new_massflow = top_massflow, new_molflow = top_molflow, aa_delta = aa_delta_column2, water_delta = water_delta_column2)

    # separation bottom
    co_delta_column2 = in_stream.co_molflow
    dco_delta_column2 = in_stream.dco_molflow
    aco_delta_column2 = in_stream.aco_molflow
    bottom_molflow = in_stream.mol_flow - top_molflow
    bottom_massflow = in_stream.mass_flow - top_massflow
    out_stream_bottom.update(new_massflow = bottom_massflow, new_molflow = bottom_molflow, co_delta = co_delta_column2, dco_delta = dco_delta_column2, aco_delta = aco_delta_column2)
    return None

def acid_separator(in_stream, recycle, purge):
    # 99mol% AA on recycle, 8mol% AA on purge
    in_stream.mol_flow = recycle.mol_flow + purge.mol_flow