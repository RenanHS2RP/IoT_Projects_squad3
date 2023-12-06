import { StyleSheet, Text, View, ActivityIndicator } from "react-native";
import React,{ useState, useEffect } from "react";
import { LineChart } from "react-native-chart-kit";
import SensorOutput from "../../components/SensorOutput";



interface SensorData {
  tempo_operacao: string;
  litros_totais: number;
}

interface ChartData {
  labels: string[];
  datasets: {
    data: number[];
    color: (opacity: number) => string;
    strokeWidth: number;
  }[];
  legend: string[];
}

const API_ENDPOINT = 'http://xquad3.pythonanywhere.com/sensor';



export default function Dashboard() {
  // Variables of output
  const [litrosTotais, setLitrosTotais] = useState(0);
  const [abastecimentoEmAndamento, setAbastecimentoEmAndamento] = useState(false);
  const [ultimaAtualizacao, setUltimaAtualizacao] = useState<Date | null>(null);

  // Variables of dashboard
  const [chartData, setChartData] = useState<ChartData>({
    labels: [],
    datasets: [
      {
        data: [],
        color: (opacity) => `rgba(134, 65, 244, ${opacity})`,
        strokeWidth: 2,
      },
    ],
    legend: ["Vazão por Segundo"],
  });
  const [loading, setLoading] = useState<boolean>(true);
  const [maxDataPoints, setMaxDataPoints] = useState<number>(7);
  const [timeInterval, setTimeInterval] = useState<number>(1);


  
  

  useEffect(() => {
    const verificaFimAbastecimento = () => {
      if (abastecimentoEmAndamento && ultimaAtualizacao) {
        const diferencaTempo = new Date().getTime() - ultimaAtualizacao.getTime();

        if (diferencaTempo > 5000 && litrosTotais > 0) {
          setAbastecimentoEmAndamento(false);
          console.log('Abastecimento concluído! Último valor:', litrosTotais);
        }
      }
    };

    const intervalFimAbastecimento = setInterval(verificaFimAbastecimento, 1000);

    return () => clearInterval(intervalFimAbastecimento);
  }, [abastecimentoEmAndamento, ultimaAtualizacao, litrosTotais]);

  useEffect(() => {
    fetchData();
    const intervalDashboard = setInterval(() => {
      fetchData();
    }, timeInterval * 1000);

    fetchDataOutput();
    const intervalOutput = setInterval(fetchDataOutput, 500);

    return () => {
      clearInterval(intervalDashboard);
      clearInterval(intervalOutput);
    }
  }, []);

    // Get data to dashboard
    const fetchData = async () => {
      try {
        const response = await fetch("http://xquad3.pythonanywhere.com/sensor/");
        const result: SensorData[] = await response.json();
  
        const formattedData = result.map((data, index) => ({
          seconds: index * timeInterval + 1,
          vazao: data.litros_totais,
        }));
  
        const reducedData = formattedData.slice(-maxDataPoints);
        const labels = reducedData.map((entry) => entry.seconds.toString());
        const vazaoPorSegundo = reducedData.map((entry) => entry.vazao);
  
        setChartData({
          labels,
          datasets: [
            {
              data: vazaoPorSegundo,
              color: (opacity) => `rgba(134, 65, 244, ${opacity})`,
              strokeWidth: 2,
            },
          ],
          legend: ["Vazão por Segundo"],
        });
  
        setLoading(false);
      } catch (error) {
        console.error("Error fetching data:", error);
        setLoading(false);
      }
    };
  
    // Code to output
    const fetchDataOutput = async () => {
      try {
        const response = await fetch(API_ENDPOINT);
        const data = await response.json();
  
        if (Array.isArray(data) && data.length > 0) {
          const ultimoDado = data[data.length - 1].litros_totais;
  
          if (ultimoDado !== litrosTotais) {
            setLitrosTotais(ultimoDado);
            setAbastecimentoEmAndamento(true);
            setUltimaAtualizacao(new Date());
          }
        }
      } catch (error) {
        console.error('Erro ao buscar dados da API:', error);
        setLitrosTotais(0);
        setAbastecimentoEmAndamento(false);
        setUltimaAtualizacao(null);
      }
    };


  if (loading) {
    return (
      <View>
        <Text>Loading...</Text>
      </View>
    );
  }


  //Lógica do abastecimento
  let textoExibicao = 'Aguardando abastecimento';

  if (abastecimentoEmAndamento) {
    textoExibicao = 'Abastecimento em andamento';
  } else if (ultimaAtualizacao) {
    textoExibicao = 'Abastecimento concluído!';
  }






  return (
    <View style={styles.container}>
         <View style={styles.container}>
          <SensorOutput value={litrosTotais} iconText={'Abastecimento aceitável'} iconColor={ 'green'} />
          <Text>{textoExibicao}</Text>
        </View>
      {loading ? (
        <ActivityIndicator size="large" color="#0000ff" />
      ) : (
        <LineChart
          data={chartData}
          width={370}
          height={220}
          chartConfig={{
            backgroundGradientFrom: "#ffffff",
            backgroundGradientTo: "#ffffff",
            color: (opacity) => `rgba(0, 0, 0, ${opacity})`,
            strokeWidth: 2,
          }}
          bezier
          xLabelsOffset={-10}
        />
      )}
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    alignSelf: "center",
    paddingTop: 40,
  },
});

