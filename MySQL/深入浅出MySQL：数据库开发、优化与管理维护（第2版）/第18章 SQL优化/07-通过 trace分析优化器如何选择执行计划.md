

MySQL 5.6提供了对SQL的跟踪 trace，通过 trace文件能够进一步了解为什么优化器选择A执行计划而不选择B执行计划，帮助我们更好地理解优化器的行为。

使用方式：首先打开trace，设置格式为JSON，设置 trace最大能够使用的内存大小，避免解析过程中因为默认内存过小而不能够完整显示。

mysql> SET OPTIMIZER_TRACE="enabled=on",END_MARKERS_IN_JSON=on;

Query OK, 0 rows affected (0.03 sec)

mysql> SET OPTIMIZER_TRACE_MAX_MEM_SIZE=1000000;

Query OK, 0 rows affected (0.00 sec)

接下来执行想做trace的SQL语句，例如想了解租赁表rental中库存编号inventory_id为4466的电影拷贝在出租日期 rental_date为 2005-05-25 4:00:00～5:00:00之间出租的记录：

mysql> select rental_id from rental where 1=1 and rental_date >= '2005-05-25 04:00:00' and rental_date <= '2005-05-25 05:00:00' and inventory_id=4466;

+-----------+

| rental_id |

+-----------+

| 39 |

+-----------+

1 row in set (0.00 sec)

最后，检查INFORMATION_SCHEMA.OPTIMIZER_TRACE就可以知道MySQL是如何执行SQL的：

mysql> SELECT * FROM INFORMATION_SCHEMA.OPTIMIZER_TRACE\G

最后会输出一个格式如下的跟踪文件：

*************************** 1. row ***************************

QUERY: select rental_id from rental where 1=1 and rental_date >='2005-05-25 04:00:00' and rental_date <= '2005-05-25 05:00:00' and inventory_id=4466

TRACE: {

"steps": [

{

"join_preparation": {

"select#": 1,

"steps": [

{

"expanded_query": "/* select#1 */ select `rental`.`rental_id` AS `rental_id`from `rental` where ((1 = 1) and (`rental`.`rental_date` >= '2005-05-25 04:00:00') and (`rental`.`rental_date` <= '2005-05-25 05:00:00') and (`rental`.`inventory_id` = 4466))"

}

] /* steps */

} /* join_preparation */

},

{

"join_optimization": {

"select#": 1,

"steps": [

{

"condition_processing": {

"condition": "WHERE",

"original_condition": "((1 = 1) and (`rental`.`rental_date` >= '2005-05-25 04:00:00') and (`rental`.`rental_date` <= '2005-05-25 05:00:00') and (`rental`.`inventory_id`= 4466))",

"steps": [

{

"transformation": "equality_propagation",

"resulting_condition": "((1 = 1) and (`rental`.`rental_date` >='2005-05-25 04:00:00') and (`rental`.`rental_date` <= '2005-05-25 05:00:00') and multiple equal(4466, `rental`.`inventory_id`))"

},

{

"transformation": "constant_propagation",

"resulting_condition": "((1 = 1) and (`rental`.`rental_date` >='2005-05-25 04:00:00') and (`rental`.`rental_date` <= '2005-05-25 05:00:00') and multiple equal(4466, `rental`.`inventory_id`))"

},

{

"transformation": "trivial_condition_removal",

"resulting_condition": "((`rental`.`rental_date` >= '2005-05-25 04:00:00') and (`rental`.`rental_date` <= '2005-05-25 05:00:00') and multiple equal(4466,`rental`.`inventory_id`))"

}

] /* steps */

} /* condition_processing */

},

{

"table_dependencies": [

{

"table": "`rental`",

"row_may_be_null": false,

"map_bit": 0,

"depends_on_map_bits": [

] /* depends_on_map_bits */

}

] /* table_dependencies */

},

{

"ref_optimizer_key_uses": [

{

"table": "`rental`",

"field": "inventory_id",

"equals": "4466",

"null_rejecting": false

}

] /* ref_optimizer_key_uses */

},

{

"rows_estimation": [

{

"table": "`rental`",

"range_analysis": {

"table_scan": {

"rows": 16005,

"cost": 3300.1

} /* table_scan */,

"potential_range_indices": [

{

"index": "PRIMARY",

"usable": false,

"cause": "not_applicable"

},

{

"index": "rental_date",

"usable": true,

"key_parts": [

"rental_date",

"inventory_id",

"customer_id"

] /* key_parts */

},

{

"index": "idx_fk_inventory_id",

"usable": true,

"key_parts": [

"inventory_id",

"rental_id"

] /* key_parts */

},

{

"index": "idx_fk_customer_id",

"usable": false,

"cause": "not_applicable"

},

{

"index": "idx_fk_staff_id",

"usable": false,

"cause": "not_applicable"

}

] /* potential_range_indices */,

"best_covering_index_scan": {

"index": "rental_date",

"cost": 3229.3,

"chosen": true

} /* best_covering_index_scan */,

"setup_range_conditions": [

] /* setup_range_conditions */,

"group_index_range": {

"chosen": false,

"cause": "not_group_by_or_distinct"

} /* group_index_range */,

"analyzing_range_alternatives": {

"range_scan_alternatives": [

{

"index": "rental_date",

"ranges": [

"2005-05-25 04:00:00 <= rental_date <= 2005-05-25 05:00:00 AND 4466<= inventory_id <= 4466"

] /* ranges */,

"index_dives_for_eq_ranges": true,

"rowid_ordered": false,

"using_mrr": false,

"index_only": true,

"rows": 10,

"cost": 3.0254,

"chosen": true

},

{

"index": "idx_fk_inventory_id",

"ranges": [

"4466 <= inventory_id <= 4466"

] /* ranges */,

"index_dives_for_eq_ranges": true,

"rowid_ordered": true,

"using_mrr": false,

"index_only": false,

"rows": 5,

"cost": 7.01,

"chosen": false,

"cause": "cost"

}

] /* range_scan_alternatives */,

"analyzing_roworder_intersect": {

"usable": false,

"cause": "too_few_roworder_scans"

} /* analyzing_roworder_intersect */

} /* analyzing_range_alternatives */,

"chosen_range_access_summary": {

"range_access_plan": {

"type": "range_scan",

"index": "rental_date",

"rows": 10,

"ranges": [

"2005-05-25 04:00:00 <= rental_date <= 2005-05-25 05:00:00 AND 4466<= inventory_id <= 4466"

] /* ranges */

} /* range_access_plan */,

"rows_for_plan": 10,

"cost_for_plan": 3.0254,

"chosen": true

} /* chosen_range_access_summary */

} /* range_analysis */

}

] /* rows_estimation */

},

{

"considered_execution_plans": [

{

"plan_prefix": [

] /* plan_prefix */,

"table": "`rental`",

"best_access_path": {

"considered_access_paths": [

{

"access_type": "ref",

"index": "idx_fk_inventory_id",

"rows": 5,

"cost": 6,

"chosen": true

},

{

"access_type": "range",

"rows": 5,

"cost": 5.0254,

"chosen": true

}

] /* considered_access_paths */

} /* best_access_path */,

"cost_for_plan": 5.0254,

"rows_for_plan": 5,

"chosen": true

}

] /* considered_execution_plans */

},

{

"attaching_conditions_to_tables": {

"original_condition": "((`rental`.`inventory_id` = 4466) and (`rental`.`rental_date` >= '2005-05-25 04:00:00') and (`rental`.`rental_date` <= '2005-05-25 05:00:00'))",

"attached_conditions_computation": [

] /* attached_conditions_computation */,

"attached_conditions_summary": [

{

"table": "`rental`",

"attached": "((`rental`.`inventory_id` = 4466) and (`rental`.`rental_date`>= '2005-05-25 04:00:00') and (`rental`.`rental_date` <= '2005-05-25 05:00:00'))"

}

] /* attached_conditions_summary */

} /* attaching_conditions_to_tables */

},

{

"refine_plan": [

{

"table": "`rental`",

"access_type": "range"

}

] /* refine_plan */

}

] /* steps */

} /* join_optimization */

},

{

"join_execution": {

"select#": 1,

"steps": [

] /* steps */

} /* join_execution */

}

] /* steps */

}

MISSING_BYTES_BEYOND_MAX_MEM_SIZE: 0

INSUFFICIENT_PRIVILEGES: 0

1 row in set (0.00 sec)



