/*
 *  Power BI Visual CLI
 *
 *  Copyright (c) Microsoft Corporation
 *  All rights reserved.
 *  MIT License
 *
 *  Permission is hereby granted, free of charge, to any person obtaining a copy
 *  of this software and associated documentation files (the ""Software""), to deal
 *  in the Software without restriction, including without limitation the rights
 *  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 *  copies of the Software, and to permit persons to whom the Software is
 *  furnished to do so, subject to the following conditions:
 *
 *  The above copyright notice and this permission notice shall be included in
 *  all copies or substantial portions of the Software.
 *
 *  THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 *  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 *  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 *  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 *  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 *  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 *  THE SOFTWARE.
 */

 module powerbi.extensibility.visual.testing97D08681EA3D4ED0A47F83D466B28D49  {
     /**
      * Interface for BarCharts viewmodel.
      *
      * @interface
      * @property {BarChartDataPoint[]} dataPoints - Set of data points the visual will render.
      * @property {number} dataMax                 - Maximum data value in the set of data points.
      */
     interface BarChartViewModel {
         dataPoints: BarChartDataPoint[];
         dataMax: number;
     };
      /**
      * Interface for BarChart data points.
      *
      * @interface
      * @property {number} value    - Data value for point.
      * @property {string} category - Coresponding category of data value.
      */
     interface BarChartDataPoint {
         value: number;
         category: string;
     };
      export class BarChart implements IVisual {
         private target: HTMLElement;
         private updateCount: number;
         private svg: d3.Selection<SVGElement>;
         private host: IVisualHost;
         private barChartContainer: d3.Selection<SVGElement>;
         private barContainer: d3.Selection<SVGElement>;
         private bars: d3.Selection<SVGElement>;
          static Config = {
             xScalePadding: 0.1,
         };
          /**
          * Creates instance of BarChart. This method is only called once.
          *
          * @constructor
          * @param {VisualConstructorOptions} options - Contains references to the element that will
          *                                             contain the visual and a reference to the host
          *                                             which contains services.
          */
         constructor(options: VisualConstructorOptions) {
             console.log('Visual constructor', options);
             this.target = options.element;
             this.updateCount = 0;
             this.host = options.host;
             let svg = this.svg = d3.select(options.element)
                 .append('svg')
                 .classed('barChart', true);
              this.barContainer = svg.append('g')
                 .classed('barContainer', true);
         }
          /**
          * Updates the state of the visual. Every sequential databinding and resize will call update.
          *
          * @function
          * @param {VisualUpdateOptions} options - Contains references to the size of the container
          *                                        and the dataView which contains all the data
          *                                        the visual had queried.
          */
         public update(options: VisualUpdateOptions) {
             console.log('Visual update', options);
             this.target.innerHTML = `<p>Update count: <em>${(this.updateCount++)}</em></p>`;
             let testData: BarChartDataPoint[] = [
                 {
                     value: 10,
                     category: 'a'
                 },
                 {
                     value: 20,
                     category: 'b'
                 },
                 {
                     value: 1,
                     category: 'c'
                 },
                 {
                     value: 100,
                     category: 'd'
                 },
                 {
                     value: 500,
                     category: 'e'
                 }];
              let viewModel: BarChartViewModel = {
                 dataPoints: testData,
                 dataMax: d3.max(testData.map((dataPoint) => dataPoint.value))
             };
              let width = options.viewport.width;
             let height = options.viewport.height;
              this.svg.attr({
                 width: width,
                 height: height
             });
              let yScale = d3.scale.linear()
                 .domain([0, viewModel.dataMax])
                 .range([height, 0]);
              let xScale = d3.scale.ordinal()
                 .domain(viewModel.dataPoints.map(d => d.category))
                 .rangeRoundBands([0, width], BarChart.Config.xScalePadding);
              let bars = this.barContainer.selectAll('.bar').data(viewModel.dataPoints);
             bars.enter()
                 .append('rect')
                 .classed('bar', true);
             bars.attr({
                 width: xScale.rangeBand(),
                 height: d => height - yScale(d.value),
                 y: d => yScale(d.value),
                 x: d => xScale(d.category)
             });
              bars.exit()
                 .remove();
         }
          /**
          * Destroy runs when the visual is removed. Any cleanup that the visual needs to
          * do should be done here.
          *
          * @function
          */
         public destroy(): void {
             //TODO: Perform any cleanup tasks here
             //Perform any cleanup tasks here
         }
     }
 } 
