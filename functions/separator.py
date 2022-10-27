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

def acid_separator(in_stream, recycle, purge, aa, water):
    'input args(in_stream, recycle stream, purge stream, chemicals:aa, water'
    # 99mol% AA on recycle, 8mol% AA on purge
    purge_mol_flow = (in_stream.mol_flow *(0.99 - in_stream.aa_frac)) / 0.91
    recycle_mol_flow = in_stream.mol_flow - purge_mol_flow

    # purge deltas
    purge_water_delta = 0.92 * purge.mol_flow
    purge_aa_delta = 0.08 * purge.mol_flow
    purge_massflow = purge_water_delta*water.mr_kg + purge_aa_delta*aa.mr_kg
    purge.update(new_massflow = purge_massflow, new_molflow = purge_mol_flow, aa_delta = purge_aa_delta, water_delta = purge_water_delta)

    # recycle deltas
    recycle_water_delta = 0.01 * recycle_mol_flow
    recycle_aa_delta = 0.99 * recycle_mol_flow
    recycle_massflow = in_stream.massflow - purge_massflow
    recycle.update(new_massflow = recycle_massflow, new_molflow = recycle_mol_flow, aa_delta = recycle_aa_delta, water_delta = recycle_water_delta)
    return None